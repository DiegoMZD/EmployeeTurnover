# Predicción de Rotación de Personal con Machine Learning

## Descripción del Proyecto

Este proyecto desarrolla un modelo de Machine Learning para predecir la rotación de personal utilizando un enfoque basado en Análisis de Supervivencia y Modelos de Aprendizaje Automático. Se han implementado distintas etapas de análisis, modelado, evaluación y despliegue de soluciones, incluyendo:

- Análisis exploratorio de datos (EDA)
- Análisis de Supervivencia (Análisis Estadístico especialmente alineado con Rotación de Personal)
- Modelamiento y evaluación
- Ajuste de hiperparámetros
- Desarrollo de una aplicación web con Streamlit
- Creación de una API con Flask
- Despliegue local de la API
- Configuración de una instancia EC2 en AWS
- Despliegue de la API en EC2

## Estructura del Proyecto

```
/
├── data/
│
├── notebooks/
│
├── models/
│
├── flask_api/
│
├── streamlit_app/
│
└── README.md  # Documento actual
```

## Requisitos

- Python 3.8+
- Bibliotecas necesarias en `requirements.txt`

## Configuración y Ejecución

### Ejecución de la API Flask (Local)

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar la API:
   ```bash
   python app.py
   ```

### Despliegue en AWS EC2

1. Subir archivos al servidor EC2:
   ```bash
   scp -i tu_clave.pem -r api ubuntu@tu_instancia:/home/ubuntu/api
   ```
2. Conectarse a la instancia EC2:
   ```bash
   ssh -i tu_clave.pem ubuntu@tu_instancia
   ```
3. Instalar dependencias dentro de la instancia:
   ```bash
   pip install -r api/requirements.txt
   ```
4. Ejecutar la API en la instancia EC2:
   ```bash
   cd api
   python app.py
   ```
5. Configurar reglas de seguridad en AWS para permitir acceso al puerto 5000.

## Pruebas de la API

Para probar la API desde Postman o desde la terminal:

```bash
curl -X POST "http://tu_instancia:5000/predict" \
-H "Content-Type: application/json" \
-d '{"feature1": valor, "feature2": valor}'
```

## Notebooks Relacionados

- [**01\_EDA.ipynb**](notebooks/01_EDA.ipynb)**:** Análisis exploratorio de datos.
- [**02\_Survival\_Analysis.ipynb**](notebooks/02_Survival_Analysis.ipynb)**:** Análisis de Supervivencia.
- [**03\_Modelling.ipynb**](notebooks/03_Modelling.ipynb)**:** Modelado y evaluación de modelos de Machine Learning.

## Autores

- DiegoMZD

## Enlace al repositorio

[GitHub - DiegoMZD/EmployeeTurnoverPrediction](https://github.com/DiegoMZD/EmployeeTurnover)