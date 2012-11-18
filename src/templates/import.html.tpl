{% extends "partials/layout.html.tpl" %}
{% block title %}Import{% endblock %}
{% block name %}Import{% endblock %}
{% block content %}
    <div class="quote">
        Please provide the file containing the database data to be imported
        to the data source.<br />
        Remember this is a <strong>dangerous operation</strong>.
    </div>
    <div class="separator-horizontal"></div>
    <div class="quote error">
        {{ error }}
    </div>
    <form enctype="multipart/form-data" action="import" method="post" class="form small">
        <div class="label">
            <label>Import File</label>
        </div>
         <div class="input">
             <a data-name="import_file" class="uploader">Select & Upload the import file</a>
        </div>
        <span class="button" data-link="{{ url_for('index') }}">Cancel</span>
        //
        <span class="button" data-submit="true">Upload</span>
    </form>
{% endblock %}