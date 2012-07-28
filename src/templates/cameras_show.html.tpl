{% extends "partials/layout_camera_f.html.tpl" %}
{% block title %}{{ camera.id }}{% endblock %}
{% block name %}{{ camera.id }}{% endblock %}
{% block content %}
    <div class="cameras single">
        {% if "resolution" in camera %}
            <img class="single" alt="{{ camera.id }}" height="{{ camera.height }}" width="{{ camera.width }}" src="{{ camera.protocol }}://{{ camera.username }}:{{ camera.password }}@{{ camera.url }}/axis-cgi/mjpg/video.cgi?camera={{ camera.camera|default(1) }}&resolution={{ camera.resolution|default('640x480') }}&compression={{ camera.compression|default(10) }}&clock={{ camera.clock|default(0) }}" />
        {% else %}
            <img class="single" alt="{{ camera.id }}" height="{{ camera.height }}" width="{{ camera.width }}" src="{{ camera.protocol }}://{{ camera.username }}:{{ camera.password }}@{{ camera.url }}/axis-cgi/mjpg/video.cgi?camera={{ camera.camera|default(1) }}&compression={{ camera.compression|default(10) }}&clock={{ camera.clock|default(0) }}" />
        {% endif %}
    </div>
{% endblock %}
