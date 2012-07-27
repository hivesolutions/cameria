{% extends "partials/layout.html.tpl" %}
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
                <td class="right label" width="50%">resolution</td>
                <td class="left value" width="50%">{{ device.settings.resolution }}</td>
            </tr>
        </tbody>
    </table>
{% endblock %}
