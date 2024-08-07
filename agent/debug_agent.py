"""Debug agent implementation"""

import os
import logging
from rich import logging as rich_logging

from ostorlab.agent.kb import kb
from ostorlab.agent import agent
from ostorlab.agent.message import message as m
from ostorlab.agent.mixins import agent_report_vulnerability_mixin

logging.basicConfig(
    format="%(message)s",
    datefmt="[%X]",
    handlers=[rich_logging.RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger(__name__)


class DebugAgent(agent.Agent, agent_report_vulnerability_mixin.AgentReportVulnMixin):
    """Debug agent."""

    def start(self) -> None:
        """Start agent method."""
        logger.info("running start")
        logger.info("environment variables %s", os.environ)
        logger.info("agent definition %s", self.definition)
        logger.info("agent settings %s", self.settings)
        self.report_vulnerability(
            entry=kb.Entry(
                title="Debug Agent",
                risk_rating="INFO",
                short_description="Debug purposes",
                description="Debug purposes",
                recommendation="",
                references={},
                security_issue=False,
                privacy_issue=False,
                has_public_exploit=False,
                targeted_by_malware=False,
                targeted_by_ransomware=False,
                targeted_by_nation_state=False,
            ),
            technical_detail="For debug",
            risk_rating=agent_report_vulnerability_mixin.RiskRating.INFO,
        )

    def process(self, message: m.Message) -> None:
        """Process messages of type v3, it emits messages of type `v3.report.vulnerability` with the
         technical report of the scan.
        Args:
            message: message containing any kind of data
        """
        logger.info("processing message %s", message)


if __name__ == "__main__":
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for l in loggers:  # noqa: E741
        l.setLevel(logging.DEBUG)
    logger.info("starting agent ...")
    DebugAgent.main()
