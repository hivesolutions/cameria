{% extends "partials/layout_device.html.tpl" %}
{% block title %}Devices{% endblock %}
{% block name %}Devices :: {{ device.name }}{% endblock %}
{% block content %}
    <div class="quote">{{ device.name }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">type</td>
                <td class="left value" width="50%">{{ device.device }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">model</td>
                <td class="left value" width="50%">{{ device.model_d }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">resolution</td>
                <td class="left value" width="50%">{{ device.resolution | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">width</td>
                <td class="left value" width="50%">{{ device.width | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">height</td>
                <td class="left value" width="50%">{{ device.height | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">fps</td>
                <td class="left value" width="50%">{{ device.fps | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">clock</td>
                <td class="left value" width="50%">{{ device.clock | default('N/A', True) }}</td>
            </tr>
        </tbody>
    </table>
{% endblock %}
