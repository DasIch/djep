# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Purchase.date_added'
        db.add_column('attendees_purchase', 'date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Purchase.date_added'
        db.delete_column('attendees_purchase', 'date_added')


    models = {
        'attendees.customer': {
            'Meta': {'ordering': "('customer_number',)", 'object_name': 'Customer'},
            'customer_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_exported': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'attendees.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['attendees.Customer']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '25'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vat_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'attendees.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['attendees.Purchase']"}),
            'ticket_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['attendees.TicketType']"}),
            'voucher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['attendees.Voucher']", 'null': 'True', 'blank': 'True'})
        },
        'attendees.tickettype': {
            'Meta': {'ordering': "('product_number', 'voucher_needed')", 'object_name': 'TicketType'},
            'date_valid_from': ('django.db.models.fields.DateTimeField', [], {}),
            'date_valid_to': ('django.db.models.fields.DateTimeField', [], {}),
            'fee': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_purchases': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'tutorial_ticket': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'voucher_needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'attendees.voucher': {
            'Meta': {'object_name': 'Voucher'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'date_valid': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'})
        }
    }

    complete_apps = ['attendees']
