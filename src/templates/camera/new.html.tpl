{% extends "partials/layout_camera_l.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}New Camera{% endblock %}
{% block content %}
    <form action="{{ url_for('create_camera') }}" method="post" class="form">
        <div class="label">
            <label>Camera ID</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="camera_id" placeholder="eg: cam_xz" value="{{ camera.camera_id }}"
                   data-error="{{ errors.camera_id }}" />
        </div>
        <div class="label">
            <label>URL</label>
        </div>
        <div class="input">
            <input class="text-field" name="url" placeholder="eg: http://cameras.com/cam_xz" value="{{ camera.url }}"
                   data-error="{{ camera.url }}" />
        </div>
        <div class="label">
            <label>Description</label>
        </div>
        <div class="input">
            <textarea class="text-area" name="description" placeholder="eg: some words about the camera"
                      data-error="{{ camera.description }}">{{ camera.description }}</textarea>
        </div>
        <div class="quote">
            By clicking Submit Camera, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Camera</span>
    </form>
{% endblock %}
