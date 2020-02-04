from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from journal.models import JournalEntry



class Command(BaseCommand):
    help = 'Generates weekly digest for companies.'

    # def add_arguments(self, parser):
    #     # Get the last Monday to pass.
    #     cal_week = CalendarWeek() - 1
    #
    #     cal_week_start_dt_default = cal_week.start.strftime('%Y-%m-%d')
    #
    #     parser.add_argument(
    #         '--cal_week_start_dt',
    #         dest='cal_week_start_dt',
    #         default=cal_week_start_dt_default,
    #         help='Monday of week to run digest for (YYYY-MM-DD)'
    #     )
    #     parser.add_argument(
    #         '--skip_digest',
    #         action='store_true',
    #         dest='skip_digest',
    #         default=False,
    #         help='Skip digest generation'
    #     )
    #     parser.add_argument(
    #         '--skip_email',
    #         action='store_true',
    #         dest='skip_email',
    #         default=False,
    #         help='Skip sending email'
    #     )

    def handle(self, *args, **options):
        cal_week_start_dt_str = options['cal_week_start_dt']
        cal_week_start_ts = timezone.datetime.strptime(cal_week_start_dt_str, '%Y-%m-%d')
        cal_week_start_dt = cal_week_start_ts.date()

        if not options['individual']:
            for user in User.objects.all():
                latest_journal_entry = JournalEntry
                send_email
        else:
            email = options['individual']
            user = User.objects.filter(email=email).first()
            if not user:
                self.stderr.write(f'User with email {email} does not exist',ending='')
                return

        self.stdout.write('email sending done.')

        if not options['skip_digest']:
            msg = f'Starting digest generation for week of {cal_week_start_dt_str} ... '
            self.stdout.write(msg, ending='')
            runner.run(cal_week_start_dt)

        if not options['skip_email']:
            self.stdout.write('Starting weekly admin digest email task')
            count = 0
            companies = Company.objects.filter(is_active=True)
            for company in companies:
                # This conditional is a hack for https://github.com/15five/fifteen5/issues/18481
                if company.digest_weekday == timezone.datetime.now().weekday():
                    count += send_weekly_admin_digest(company, cal_week_start_dt)
            self.stdout.write(f'Sent emails to {count} companies for weekly admin digest email task')
