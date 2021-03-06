<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'mail_notification';
$app['version'] = '2.3.22';
$app['release'] = '1';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['summary'] = lang('mail_notification_app_description');
$app['description'] = lang('mail_notification_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('mail_notification_app_name');
$app['category'] = lang('base_category_system');
$app['subcategory'] = lang('base_subcategory_settings');
$app['menu_enabled'] = FALSE;

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['core_only'] = TRUE;

$app['core_requires'] = array(
    'app-network-core >= 1:1.2.10',
    'app-mail',
    'Swift',
);

$app['core_file_manifest'] = array(
    'mail_notification.conf' => array(
        'target' => '/etc/clearos/mail_notification.conf',
        'mode' => '0600',
        'config' => TRUE,
        'config_params' => 'noreplace',
    ),
);
