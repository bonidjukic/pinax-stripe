# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 19:00
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import pinax.stripe.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('business_name', models.TextField(blank=True, null=True)),
                ('business_url', models.TextField(blank=True, null=True)),
                ('charges_enabled', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=2)),
                ('debit_negative_balances', models.BooleanField(default=False)),
                ('decline_charge_on_avs_failure', models.BooleanField(default=False)),
                ('decline_charge_on_cvc_failure', models.BooleanField(default=False)),
                ('default_currency', models.CharField(max_length=3)),
                ('details_submitted', models.BooleanField(default=False)),
                ('display_name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('legal_entity_address_city', models.TextField(blank=True, null=True)),
                ('legal_entity_address_country', models.TextField(blank=True, null=True)),
                ('legal_entity_address_line1', models.TextField(blank=True, null=True)),
                ('legal_entity_address_line2', models.TextField(blank=True, null=True)),
                ('legal_entity_address_postal_code', models.TextField(blank=True, null=True)),
                ('legal_entity_address_state', models.TextField(blank=True, null=True)),
                ('legal_entity_dob', models.DateField(blank=True, null=True)),
                ('legal_entity_first_name', models.TextField(blank=True, null=True)),
                ('legal_entity_gender', models.TextField(blank=True, null=True)),
                ('legal_entity_last_name', models.TextField(blank=True, null=True)),
                ('legal_entity_maiden_name', models.TextField(blank=True, null=True)),
                ('legal_entity_personal_id_number_provided', models.BooleanField(default=False)),
                ('legal_entity_phone_number', models.TextField(blank=True, null=True)),
                ('legal_entity_ssn_last_4_provided', models.BooleanField(default=False)),
                ('legal_entity_type', models.TextField(blank=True, null=True)),
                ('legal_entity_verification_details', models.TextField(blank=True, null=True)),
                ('legal_entity_verification_details_code', models.TextField(blank=True, null=True)),
                ('legal_entity_verification_document', models.TextField(blank=True, null=True)),
                ('legal_entity_verification_status', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('metadata', jsonfield.fields.JSONField(blank=True, null=True)),
                ('stripe_publishable_key', models.CharField(blank=True, max_length=100, null=True)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('statement_descriptor', models.TextField(blank=True, null=True)),
                ('support_email', models.TextField(blank=True, null=True)),
                ('support_phone', models.TextField(blank=True, null=True)),
                ('timezone', models.TextField(blank=True, null=True)),
                ('tos_acceptance_date', models.DateField(blank=True, null=True)),
                ('tos_acceptance_ip', models.TextField(blank=True, null=True)),
                ('tos_acceptance_user_agent', models.TextField(blank=True, null=True)),
                ('payout_schedule_delay_days', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('payout_schedule_interval', models.CharField(blank=True, choices=[('Manual', 'manual'), ('Daily', 'daily'), ('Weekly', 'weekly'), ('Monthly', 'monthly')], max_length=7, null=True)),
                ('payout_schedule_monthly_anchor', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('payout_schedule_weekly_anchor', models.TextField(blank=True, null=True)),
                ('payout_statement_descriptor', models.TextField(blank=True, null=True)),
                ('payouts_enabled', models.BooleanField(default=False)),
                ('verification_disabled_reason', models.TextField(blank=True, null=True)),
                ('verification_due_by', models.DateTimeField(blank=True, null=True)),
                ('verification_timestamp', models.DateTimeField(blank=True, null=True)),
                ('verification_fields_needed', jsonfield.fields.JSONField(blank=True, null=True)),
                ('authorized', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stripe_accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('account_holder_name', models.TextField()),
                ('account_holder_type', models.TextField()),
                ('bank_name', models.TextField(blank=True, null=True)),
                ('country', models.TextField()),
                ('currency', models.TextField()),
                ('default_for_currency', models.BooleanField(default=False)),
                ('fingerprint', models.TextField()),
                ('last4', models.CharField(max_length=4)),
                ('metadata', jsonfield.fields.JSONField(blank=True, null=True)),
                ('routing_number', models.TextField()),
                ('status', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to='pinax_stripe.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BitcoinReceiver',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount_received', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
                ('bitcoin_amount', models.PositiveIntegerField()),
                ('bitcoin_amount_received', models.PositiveIntegerField(default=0)),
                ('bitcoin_uri', models.TextField(blank=True)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('description', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('filled', models.BooleanField(default=False)),
                ('inbound_address', models.TextField(blank=True)),
                ('payment', models.TextField(blank=True)),
                ('refund_address', models.TextField(blank=True)),
                ('uncaptured_funds', models.BooleanField(default=False)),
                ('used_for_payment', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.TextField(blank=True)),
                ('address_line_1', models.TextField(blank=True)),
                ('address_line_1_check', models.CharField(max_length=15)),
                ('address_line_2', models.TextField(blank=True)),
                ('address_city', models.TextField(blank=True)),
                ('address_state', models.TextField(blank=True)),
                ('address_country', models.TextField(blank=True)),
                ('address_zip', models.TextField(blank=True)),
                ('address_zip_check', models.CharField(max_length=15)),
                ('brand', models.TextField(blank=True)),
                ('country', models.CharField(blank=True, max_length=2)),
                ('cvc_check', models.CharField(blank=True, max_length=15)),
                ('dynamic_last4', models.CharField(blank=True, max_length=4)),
                ('tokenization_method', models.CharField(blank=True, max_length=15)),
                ('exp_month', models.IntegerField()),
                ('exp_year', models.IntegerField()),
                ('funding', models.CharField(max_length=15)),
                ('last4', models.CharField(blank=True, max_length=4)),
                ('fingerprint', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('amount_refunded', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('description', models.TextField(blank=True)),
                ('paid', models.NullBooleanField()),
                ('disputed', models.NullBooleanField()),
                ('refunded', models.NullBooleanField()),
                ('captured', models.NullBooleanField()),
                ('receipt_sent', models.BooleanField(default=False)),
                ('charge_created', models.DateTimeField(blank=True, null=True)),
                ('available', models.BooleanField(default=False)),
                ('available_on', models.DateTimeField(blank=True, null=True)),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('fee_currency', models.CharField(blank=True, max_length=10, null=True)),
                ('transfer_group', models.TextField(blank=True, null=True)),
                ('outcome', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(pinax.stripe.models.StripeAccountFromCustomerMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount_off', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('duration', models.CharField(default='once', max_length=10)),
                ('duration_in_months', models.PositiveIntegerField(blank=True, null=True)),
                ('livemode', models.BooleanField(default=False)),
                ('max_redemptions', models.PositiveIntegerField(blank=True, null=True)),
                ('metadata', jsonfield.fields.JSONField(blank=True, null=True)),
                ('percent_off', models.PositiveIntegerField(blank=True, null=True)),
                ('redeem_by', models.DateTimeField(blank=True, null=True)),
                ('times_redeemed', models.PositiveIntegerField(blank=True, null=True)),
                ('valid', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('account_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('currency', models.CharField(blank=True, default='usd', max_length=10)),
                ('delinquent', models.BooleanField(default=False)),
                ('default_source', models.TextField(blank=True)),
                ('date_purged', models.DateTimeField(blank=True, editable=False, null=True)),
                ('stripe_account', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Account')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('kind', models.CharField(max_length=250)),
                ('livemode', models.BooleanField(default=False)),
                ('webhook_message', jsonfield.fields.JSONField()),
                ('validated_message', jsonfield.fields.JSONField(blank=True, null=True)),
                ('valid', models.NullBooleanField()),
                ('processed', models.BooleanField(default=False)),
                ('request', models.CharField(blank=True, max_length=100)),
                ('pending_webhooks', models.PositiveIntegerField(default=0)),
                ('api_version', models.CharField(blank=True, max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Customer')),
                ('stripe_account', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventProcessingException',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('data', models.TextField()),
                ('message', models.CharField(max_length=500)),
                ('traceback', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=9)),
                ('attempted', models.NullBooleanField()),
                ('attempt_count', models.PositiveIntegerField(blank=True, null=True)),
                ('statement_descriptor', models.TextField(blank=True)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('closed', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('paid', models.BooleanField(default=False)),
                ('receipt_number', models.TextField(blank=True)),
                ('period_end', models.DateTimeField()),
                ('period_start', models.DateTimeField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=9)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('tax_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date', models.DateTimeField()),
                ('webhooks_delivered_at', models.DateTimeField(blank=True, null=True)),
                ('charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='pinax_stripe.Charge')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='pinax_stripe.Customer')),
            ],
            options={
                'abstract': False,
            },
            bases=(pinax.stripe.models.StripeAccountFromCustomerMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('kind', models.CharField(blank=True, max_length=25)),
                ('period_start', models.DateTimeField()),
                ('period_end', models.DateTimeField()),
                ('proration', models.BooleanField(default=False)),
                ('line_type', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pinax_stripe.Invoice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(max_length=15)),
                ('interval', models.CharField(max_length=15)),
                ('interval_count', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('statement_descriptor', models.TextField(blank=True)),
                ('trial_period_days', models.IntegerField(blank=True, null=True)),
                ('metadata', jsonfield.fields.JSONField(blank=True, null=True)),
                ('stripe_account', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('application_fee_percent', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=3, null=True)),
                ('cancel_at_period_end', models.BooleanField(default=False)),
                ('canceled_at', models.DateTimeField(blank=True, null=True)),
                ('current_period_end', models.DateTimeField(blank=True, null=True)),
                ('current_period_start', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('status', models.CharField(max_length=25)),
                ('trial_end', models.DateTimeField(blank=True, null=True)),
                ('trial_start', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Customer')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Plan')),
            ],
            options={
                'abstract': False,
            },
            bases=(pinax.stripe.models.StripeAccountFromCustomerMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount_reversed', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('application_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('currency', models.CharField(default='usd', max_length=25)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('destination', models.TextField(blank=True, null=True)),
                ('destination_payment', models.TextField(blank=True, null=True)),
                ('failure_code', models.TextField(blank=True, null=True)),
                ('failure_message', models.TextField(blank=True, null=True)),
                ('livemode', models.BooleanField(default=False)),
                ('metadata', jsonfield.fields.JSONField(blank=True, null=True)),
                ('method', models.TextField(blank=True, null=True)),
                ('reversed', models.BooleanField(default=False)),
                ('source_transaction', models.TextField(blank=True, null=True)),
                ('source_type', models.TextField(blank=True, null=True)),
                ('statement_descriptor', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=25)),
                ('transfer_group', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfers', to='pinax_stripe.Event')),
                ('stripe_account', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransferChargeFee',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('application', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('kind', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charge_fee_details', to='pinax_stripe.Transfer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_accounts', related_query_name='user_account', to='pinax_stripe.Account')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_accounts', related_query_name='user_account', to='pinax_stripe.Customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_accounts', related_query_name='user_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Plan'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Subscription'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Subscription'),
        ),
        migrations.AddField(
            model_name='customer',
            name='users',
            field=models.ManyToManyField(related_name='customers', related_query_name='customers', through='pinax_stripe.UserAccount', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='charge',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charges', to='pinax_stripe.Customer'),
        ),
        migrations.AddField(
            model_name='charge',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charges', to='pinax_stripe.Invoice'),
        ),
        migrations.AddField(
            model_name='card',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Customer'),
        ),
        migrations.AddField(
            model_name='bitcoinreceiver',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Customer'),
        ),
        migrations.AlterUniqueTogether(
            name='useraccount',
            unique_together=set([('user', 'account')]),
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together=set([('stripe_id', 'stripe_account')]),
        ),
    ]
