"""Unittests for agent."""
from ostorlab.agent.mixins import agent_report_vulnerability_mixin
from ostorlab.agent import definitions as agent_definitions
from ostorlab.agent import message
from ostorlab.runtimes import definitions as runtime_definitions
from ostorlab.agent.kb import kb

from agent import debug_agent


def testDebugAgent_Always_ShouldCallReportVuln(mocker):
    """Test Debug agent when receiving a message."""
    msg = message.Message.from_data(selector='v3.asset.ip.v4', data={'version': 15631, 'host': '0.0.0.0'})
    definition = agent_definitions.AgentDefinition(name='start_test_agent', out_selectors=['v3.report.vulnerability'])
    settings = runtime_definitions.AgentSettings(key='agent/ostorlab/debug_agent')
    test_agent = debug_agent.DebugAgent(definition, settings)
    mock_report_vulnerability = mocker.patch('agent.debug_agent.DebugAgent.report_vulnerability', return_value=None)
    test_agent.process(msg)
    kb_entry = kb.Entry(
        title='Debug Agent',
        risk_rating='INFO',
        short_description='Debug purposes',
        description='Debug purposes',
        recommendation='',
        references={},
        security_issue=False,
        privacy_issue=False,
        has_public_exploit=False,
        targeted_by_malware=False,
        targeted_by_ransomware=False,
        targeted_by_nation_state=False
                    )
    mock_report_vulnerability.assert_called_once_with(entry=kb_entry,
        technical_detail=str(msg), risk_rating=agent_report_vulnerability_mixin.RiskRating.INFO)

