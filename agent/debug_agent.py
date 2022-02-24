"""Debug agent implementation"""
import logging
from rich import logging as rich_logging

from ostorlab.agent.kb import kb
from ostorlab.agent import agent
from ostorlab.agent import message as m
from ostorlab.agent.mixins import agent_report_vulnerability_mixin

logging.basicConfig(
    format='%(message)s',
    datefmt='[%X]',
    handlers=[rich_logging.RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger(__name__)
logger.setLevel('INFO')


class DebugAgent(agent.Agent, agent_report_vulnerability_mixin.AgentReportVulnMixin):
    """Debug agent."""

    def start(self) -> None:
        """Start agent method."""
        logger.info('running start')

    def process(self, message: m.Message) -> None:
        """Process messages of type v3, it emits messages of type `v3.report.vulnerability` with the
         technical report of the scan.
        Args:
            message: message containing any kind of data
        """
        logger.info('processing message')
        self.report_vulnerability(entry=kb.Entry(
                        title='Debug Agent',
                        risk_rating='INFO',
                        short_description='Debug purposes',
                        description='Debug purposes',
                        recommendation = '',
                        references = {},
                        security_issue = False,
                        privacy_issue = False,
                        has_public_exploit = False,
                        targeted_by_malware = False,
                        targeted_by_ransomware = False,
                        targeted_by_nation_state = False
                    ),
                    technical_detail=str(message),
                    risk_rating=agent_report_vulnerability_mixin.RiskRating.INFO)


if __name__ == '__main__':
    logger.info('starting agent ...')
    DebugAgent.main()
