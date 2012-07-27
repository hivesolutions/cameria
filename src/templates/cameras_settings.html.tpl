{% extends "partials/layout.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}Cameras :: {{ camera.id }}{% endblock %}
{% block content %}
    <div class="quote capitalize">{{ camera.id }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">type</td>
                <td class="left value" width="50%">{{ camera.type }}</td>
            </tr>
        </tbody>
    </table>
{% endblock %}
