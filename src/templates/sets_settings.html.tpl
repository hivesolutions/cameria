{% extends "partials/layout_set.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}Sets :: {{ set.name }}{% endblock %}
{% block content %}
    <div class="quote capitalize">{{ set.id }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">resolution</td>
                <td class="left value" width="50%">{{ set.camera.resolution }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">width</td>
                <td class="left value" width="50%">{{ set.camera.width }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">height</td>
                <td class="left value" width="50%">{{ set.camera.height }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">compression</td>
                <td class="left value" width="50%">{{ set.camera.compression }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">fps</td>
                <td class="left value" width="50%">{{ set.camera.fps }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">clock</td>
                <td class="left value" width="50%">{{ set.camera.clock }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">cameras</td>
                <td class="left value" width="50%">
                    {% for camera in set.cameras %}
                        <a href="{{ url_for('show_camera', id = camera.id) }}">{{ camera.id }}</a>{% if not loop.last %},{% endif %}
                    {% endfor %}
                </td>
            </tr>
        </tbody>
    </table>
{% endblock %}
