{% extends "partials/layout_set_f.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}Sets :: {{ set.name }}{% endblock %}
{% block content %}
    <div class="cameras">
        {% for camera in set.cameras %}
            <a href="{{ url_for('show_camera', id = camera.id) }}">
                {% if "resolution" in camera %}
                    <img alt="{{ camera.id }}" height="{{ camera.height }}" width="{{ camera.width }}" src="{{ camera.protocol }}://{{ camera.username }}:{{ camera.password }}@{{ camera.url }}/axis-cgi/mjpg/video.cgi?camera={{ camera.camera|default(1) }}&resolution={{ camera.resolution|default('640x480') }}&compression={{ camera.compression|default(10) }}&fps={{ camera.fps|default(10) }}&clock={{ camera.clock|default(0) }}" />
                {% else %}
                    <img alt="{{ camera.id }}" height="{{ camera.height }}" width="{{ camera.width }}" src="{{ camera.protocol }}://{{ camera.username }}:{{ camera.password }}@{{ camera.url }}/axis-cgi/mjpg/video.cgi?camera={{ camera.camera|default(1) }}&compression={{ camera.compression|default(10) }}&fps={{ camera.fps|default(10) }}&clock={{ camera.clock|default(0) }}" />
                {% endif %}
            </a>
        {% endfor %}
    </div>
{% endblock %}
