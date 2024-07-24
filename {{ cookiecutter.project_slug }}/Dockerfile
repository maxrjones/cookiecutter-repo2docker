# Inherit from a JupyterHub compatible Docker image
FROM {{ cookiecutter.base_image }}:{{ cookiecutter.base_image_tag }}

{%- if cookiecutter.add_conda_packages == 'y' %}

# Add conda packages
COPY environment.yml /tmp/environment.yml
RUN mamba env update --prefix ${CONDA_DIR} --file /tmp/environment.yml
{%- endif %}
