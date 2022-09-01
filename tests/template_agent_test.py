"""Unittests for agent."""
from ostorlab.agent import definitions as agent_definitions
from ostorlab.agent.message import message
from ostorlab.runtimes import definitions as runtime_definitions

from agent import debug_agent


def testDebugAgent_Always_ShouldCallReportVuln(mocker):
    """Test Debug agent when receiving a message."""
    msg = message.Message.from_data(selector='v3.asset.ip.v4', data={'version': 15631, 'host': '0.0.0.0'})
    definition = agent_definitions.AgentDefinition(name='start_test_agent', out_selectors=['v3.report.vulnerability'])
    settings = runtime_definitions.AgentSettings(key='agent/ostorlab/debug_agent')
    test_agent = debug_agent.DebugAgent(definition, settings)
    mock_report_vulnerability = mocker.patch('logging.Logger.info', return_value=None)
    test_agent.process(msg)
    mock_report_vulnerability.assert_called_once_with('processing message %s', msg)

