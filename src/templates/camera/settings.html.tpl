{% extends "partials/layout_camera.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}Cameras :: {{ camera.camera_id }}{% endblock %}
{% block content %}
    <div class="quote">{{ camera.camera_id }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">type</td>
                <td class="left value" width="50%">{{ camera.type }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">model</td>
                <td class="left value" width="50%">{{ camera.model_ }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">url</td>
                <td class="left value" width="50%">{{ camera.url }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">protocol</td>
                <td class="left value" width="50%">{{ camera.protocol }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">camera</td>
                <td class="left value" width="50%">{{ camera.camera }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">username</td>
                <td class="left value" width="50%">{{ camera.username }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">compression</td>
                <td class="left value" width="50%">{{ camera.compression }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">fps</td>
                <td class="left value" width="50%">{{ camera.fps }}</td>
            </tr>
        </tbody>
    </table>
{% endblock %}
