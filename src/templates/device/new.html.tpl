{% extends "partials/layout_device_l.html.tpl" %}
{% block title %}Devices{% endblock %}
{% block name %}New Device{% endblock %}
{% block content %}
    <form action="{{ url_for('create_device') }}" method="post" class="form">
        <div class="label">
            <label>Device ID</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="device_id" placeholder="eg: device_xz" value="{{ device.device_id }}"
                   data-error="{{ errors.device_id }}" />
        </div>
        <div class="label">
            <label>Type</label>
        </div>
        <div class="input">
            <input class="text-field" name="type" placeholder="eg: axis" value="{{ device.type }}"
                   data-error="{{ errors.type }}" />
        </div>
        <div class="label">
            <label>Model</label>
        </div>
        <div class="input">
            <input class="text-field" name="model" placeholder="eg: 211" value="{{ device.model }}"
                   data-error="{{ errors.model }}" />
        </div>
        <div class="label">
            <label>Device</label>
        </div>
        <div class="input">
            <div name="device" class="drop-field drop-field-select" value="{{ device.device | default('camera') }}"
                 data-error="{{ errors.device }}">
                <ul class="data-source" data-type="local">
                    <li>camera</li>
                    <li>encoder</li>
                </ul>
            </div>
        </div>
        <div class="input">
            <div class="option">
                <span class="float-left">Provide resolution support ?</span>
                <input class="float-right" type="checkbox" name="resolution" checked="1" />
                <div class="clear"></div>
            </div>
        </div>
        <div class="quote">
            By clicking Submit Device, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Device</span>
    </form>
{% endblock %}
