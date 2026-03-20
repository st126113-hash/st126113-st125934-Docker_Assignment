from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    saved_objects = pickle.load(f)

model = saved_objects['model']
model_encoder = saved_objects.get('model_encoder')
region_encoder = saved_objects.get('region_encoder')
feature_columns = saved_objects.get('feature_columns', ['Year', 'Region', 'Model'])


def safe_transform(encoder, value, field_name):
    if encoder is None:
        raise ValueError(f'{field_name} encoder is missing in model.pkl')

    classes = list(getattr(encoder, 'classes_', []))
    if value not in classes:
        raise ValueError(
            f"Unknown {field_name}: '{value}'. Available values include: {', '.join(classes[:10])}"
        )
    return int(encoder.transform([value])[0])


@app.route('/')
def home():
    model_options = []
    region_options = []

    if model_encoder is not None and hasattr(model_encoder, 'classes_'):
        model_options = sorted(model_encoder.classes_.tolist())

    if region_encoder is not None and hasattr(region_encoder, 'classes_'):
        region_options = sorted(region_encoder.classes_.tolist())

    return render_template(
        'index.html',
        model_options=model_options,
        region_options=region_options,
    )


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        model_name = str(data.get('Model', '')).strip()
        region_name = str(data.get('Region', '')).strip()
        year_value = data.get('Year')

        if not model_name or not region_name or year_value in [None, '']:
            return jsonify({'error': 'Please provide Model, Year, and Region.'}), 400

        try:
            year_value = int(year_value)
        except (TypeError, ValueError):
            return jsonify({'error': 'Year must be a valid number.'}), 400

        model_value = safe_transform(model_encoder, model_name, 'Model')
        region_value = safe_transform(region_encoder, region_name, 'Region')

        input_df = pd.DataFrame([
            {
                'Year': year_value,
                'Region': region_value,
                'Model': model_value,
            }
        ])

        input_df = input_df[feature_columns]
        prediction = int(model.predict(input_df)[0])
        label = 'High Sales' if prediction == 1 else 'Low Sales'

        return jsonify(
            {
                'label': label,
                'model': model_name,
                'year': year_value,
                'region': region_name,
                'message': f"Prediction for {model_name} in {region_name} ({year_value}): {label}",
            }
        )

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
