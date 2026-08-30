from client import OsGuiDesktopAutomationVisionAgentClient

def main():
    client = OsGuiDesktopAutomationVisionAgentClient()
    res = client.execute_desktop_action('https://assets.genpark.ai/desktop/browser_crm.png', 'Open customer profile #8892 and export invoice')
    print('OS GUI Vision Agent: ' + res['action_plan_id'] + ' (Resolution: ' + res['target_screen_resolution'] + ')')
    print('Action Steps: ' + str(len(res['keyboard_mouse_action_sequence'])) + ' | Grounding Accuracy: ' + str(res['visual_grounding_accuracy_pct']) + '%')
    for step in res['keyboard_mouse_action_sequence']:
        print('  - ' + str(step))
    print('Trace URL: ' + res['execution_audit_trace_url'])

if __name__ == '__main__':
    main()
