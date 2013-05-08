{% extends "partials/layout_set_l.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}New Set{% endblock %}
{% block content %}
    <form action="{{ url_for('create_set') }}" method="post" class="form">
        <div class="label">
            <label>Set ID</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="set_id" placeholder="eg: set_xz" value="{{ set.set_id }}"
                   data-error="{{ errors.set_id }}" />
        </div>
        <div class="label">
            <label>Name</label>
        </div>
        <div class="input">
            <input class="text-field" name="name" placeholder="eg: The office set" value="{{ set.name }}"
                   data-error="{{ errors.name }}" />
        </div>
        <div class="label">
            <label>Resolution</label>
        </div>
        <div class="input">
            <input class="text-field" name="resolution" placeholder="eg: 320x240" value="{{ set.resolution }}"
                   data-error="{{ errors.resolution }}" />
        </div>
        <div class="label">
            <label>Width</label>
        </div>
        <div class="input">
            <input class="text-field" name="width" placeholder="eg: 320" value="{{ set.width }}"
                   data-error="{{ errors.width }}" />
        </div>
        <div class="label">
            <label>Height</label>
        </div>
        <div class="input">
            <input class="text-field" name="height" placeholder="eg: 240" value="{{ set.height }}"
                   data-error="{{ errors.height }}" />
        </div>
        <div class="label">
            <label>Compression</label>
        </div>
        <div class="input">
            <input class="text-field" name="compression" placeholder="eg: 50" value="{{ set.compression }}"
                   data-error="{{ errors.compression }}" />
        </div>
        <div class="label">
            <label>Fps</label>
        </div>
        <div class="input">
            <input class="text-field" name="fps" placeholder="eg: 1" value="{{ set.fps }}"
                   data-error="{{ errors.fps }}" />
        </div>
        <div class="label">
            <label>Clock</label>
        </div>
        <div class="input">
            <input class="text-field" name="clock" placeholder="eg: 0" value="{{ set.clock }}"
                   data-error="{{ errors.clock }}" />
        </div>
        <div class="label">
            <label>Cameras</label>
        </div>
        <div class="input">
            <div name="cameras" class="tag-field" data-display_attribute="camera_id"
                 data-value_attribute="camera_id" data-error="{{ errors.cameras }}">
                <input name="cameras" type="hidden" class="tag-empty-field" />
                <ul class="tags">
                    {% for camera in set.cameras.objects %}
                        <li>{{ camera.camera_id }}</li>
                    {% endfor %}
                </ul>
                <ul class="data-source" data-url="{{ url_for('list_cameras_json') }}" data-type="json"></ul>
            </div>
        </div>
        <div class="quote">
            By clicking Submit Set, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Set</span>
    </form>
{% endblock %}
