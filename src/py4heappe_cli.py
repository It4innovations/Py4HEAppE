import typer

import py4heappe.heappe_v5.cli.auth as auth
import py4heappe.heappe_v5.cli.command_template as command_template
import py4heappe.heappe_v5.cli.configuration as configuration
import py4heappe.heappe_v5.cli.information as information
import py4heappe.heappe_v5.cli.job_management as job_management
import py4heappe.heappe_v5.cli.report as report

app = typer.Typer(no_args_is_help=True, pretty_exceptions_short=True, pretty_exceptions_show_locals=False)
app.add_typer(configuration.app, name="Conf", help="Configuration options")
app.add_typer(auth.app, name="Auth", help="Authentication methods")
app.add_typer(command_template.app, name="CmdTemp", help="Command templates management")
app.add_typer(information.app, name="Info", help="Information")
#app.add_typer(job_management.app, name="JobMgmt", help="HEAppE Job Management")
app.add_typer(report.app, name="Report", help="Reporting and usage")

def main():
    app()

if __name__ == '__main__':
    main()