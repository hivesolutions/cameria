{% extends "partials/layout_set.html.tpl" %}
{% block title %}Sets{% endblock %}
{% block name %}Sets :: {{ set.name }}{% endblock %}
{% block content %}
    <div class="quote">{{ set.set_id }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">resolution</td>
                <td class="left value" width="50%">{{ set.resolution | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">width</td>
                <td class="left value" width="50%">{{ set.width | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">height</td>
                <td class="left value" width="50%">{{ set.height | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">compression</td>
                <td class="left value" width="50%">{{ set.compression | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">fps</td>
                <td class="left value" width="50%">{{ set.fps | default('N/A', True) }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">clock</td>
                <td class="left value" width="50%">{{ set.clock | default('N/A') }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">cameras</td>
                <td class="left value" width="50%">
                    {% for camera in set.cameras.objects %}
                        <a href="{{ url_for('show_camera', camera_id = camera.camera_id) }}">{{ camera.id }}</a>{% if not loop.last %},{% endif %}
                    {% endfor %}
                </td>
            </tr>
        </tbody>
    </table>
{% endblock %}
