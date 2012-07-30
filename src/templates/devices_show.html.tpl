{% extends "partials/layout_device.html.tpl" %}
{% block title %}Devices{% endblock %}
{% block name %}{{ device.type }} {{ device.model }}{% endblock %}
{% block content %}
    <div class="quote capitalize">{{ device.type }} {{ device.model }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">type</td>
                <td class="left value" width="50%">{{ device.device }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">model</td>
                <td class="left value" width="50%">{{ device.model }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">resolution</td>
                <td class="left value" width="50%">{{ device.camera.resolution }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">width</td>
                <td class="left value" width="50%">{{ device.camera.width }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">width</td>
                <td class="left value" width="50%">{{ device.camera.width }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">fps</td>
                <td class="left value" width="50%">{{ device.camera.fps }}</td>
            </tr>
        </tbody>
    </table>
{% endblock %}
