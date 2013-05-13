{% extends "partials/layout_account.html.tpl" %}
{% block title %}Accounts{% endblock %}
{% block name %}Accounts :: {{ account.username }}{% endblock %}
{% block content %}
    <form action="{{ url_for('update_account', username = account.username) }}" method="post" class="form">
        <div class="label">
            <label>Username</label>
        </div>
        <div class="input">
            <input class="text-field" name="username" placeholder="eg: johndoe" value="{{ account.username }}"
                   data-disabled="1" data-error="{{ errors.username }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" placeholder="eg: jonhdoepass"
                   value="{{ account.password }}" data-error="{{ errors.password }}" />
        </div>
        <div class="label">
            <label>Confirm Password</label>
        </div>
        <div class="input">
            <input  type="password" class="text-field" name="password_confirm" placeholder="eg: jonhdoepass"
                    value="{{ account.password_confirm }}" data-error="{{ errors.password_confirm }}" />
        </div>
        <div class="label">
            <label>Email</label>
        </div>
        <div class="input">
            <input class="text-field" name="email" placeholder="eg: johndoe@example.com" value="{{ account.email }}"
                   data-error="{{ errors.email }}" />
        </div>
        <div class="label">
            <label>Type</label>
        </div>
        <div class="input left">
            {% if account.type == 1 or not account.type %}
                <input type="radio" name="type" id="user" value="1" checked="1" />
            {% else %}
                <input type="radio" name="type" id="user" value="1" />
            {% endif %}
            <label class="radio-label" for="user">User</label>
            {% if account.type == 2 %}
                <input type="radio" name="type" id="super_user" value="2" checked="1" />
            {% else %}
                <input type="radio" name="type" id="super_user" value="2" />
            {% endif %}
            <label class="radio-label" for="super_user">Super User</label>
            {% if account.type == 3 %}
                <input type="radio" name="type" id="admin" value="3" checked="1" />
            {% else %}
                <input type="radio" name="type" id="admin" value="3" />
            {% endif %}
            <label class="radio-label" for="admin">Admin</label>
        </div>
        <div class="label">
            <label>Cameras</label>
        </div>
        <div class="input">
            <div name="cameras" class="tag-field" data-display_attribute="camera_id"
                 data-value_attribute="camera_id" data-error="{{ errors.cameras }}">
                <input name="cameras" type="hidden" class="tag-empty-field" />
                <ul class="tags">
                    {% for camera in account.cameras.objects %}
                        <li>{{ camera.camera_id }}</li>
                    {% endfor %}
                </ul>
                <ul class="data-source" data-url="{{ url_for('list_cameras_json') }}" data-type="json"></ul>
            </div>
        </div>
        <span class="button" data-link="{{ url_for('show_account', username = account.username) }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
