import typer

import py4heappe.cli.auth as auth
import py4heappe.cli.command_template as command_template
import py4heappe.cli.configuration as configuration
import py4heappe.cli.information as information
import py4heappe.cli.job_management as job_management
import py4heappe.cli.report as report

app = typer.Typer(no_args_is_help=True, pretty_exceptions_short=True, pretty_exceptions_show_locals=False)
app.add_typer(configuration.app, name="Config", help="HEAppE Configuration")
app.add_typer(auth.app, name="Auth", help="HEAppE Authentication Methods")
app.add_typer(command_template.app, name="CmdTemplateMgmt", help="HEAppE Command Templates Management")
app.add_typer(information.app, name="Info", help="HEAppE Information")
#app.add_typer(job_management.app, name="JobMgmt", help="HEAppE Job Management")
app.add_typer(report.app, name="Report", help="HEAppE Reporting Methods")

def main():
    app()

if __name__ == '__main__':
    main()