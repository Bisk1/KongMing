# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lesson'
        db.create_table(u'chinesetool_lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'chinesetool', ['Lesson'])

        # Adding model 'WordPL'
        db.create_table(u'chinesetool_wordpl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'chinesetool', ['WordPL'])

        # Adding model 'WordZH'
        db.create_table(u'chinesetool_wordzh', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('pinyin', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['chinesetool.Lesson'], null=True)),
        ))
        db.send_create_signal(u'chinesetool', ['WordZH'])

        # Adding unique constraint on 'WordZH', fields ['word', 'pinyin']
        db.create_unique(u'chinesetool_wordzh', ['word', 'pinyin'])

        # Adding model 'WordTranslation'
        db.create_table(u'chinesetool_wordtranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word_zh', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordZH'])),
            ('word_pl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordPL'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordTranslation'])

        # Adding unique constraint on 'WordTranslation', fields ['word_zh', 'word_pl']
        db.create_unique(u'chinesetool_wordtranslation', ['word_zh_id', 'word_pl_id'])

        # Adding model 'SentencePL'
        db.create_table(u'chinesetool_sentencepl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sentence', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'chinesetool', ['SentencePL'])

        # Adding model 'SentenceZH'
        db.create_table(u'chinesetool_sentencezh', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sentence', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'chinesetool', ['SentenceZH'])

        # Adding model 'SentenceTranslation'
        db.create_table(u'chinesetool_sentencetranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sentence_zh', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordZH'])),
            ('sentence_pl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordPL'])),
        ))
        db.send_create_signal(u'chinesetool', ['SentenceTranslation'])

        # Adding model 'Abonament'
        db.create_table(u'chinesetool_abonament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('registration_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_login_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('abo_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'chinesetool', ['Abonament'])

        # Adding model 'WordSkills'
        db.create_table(u'chinesetool_wordskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word_zh', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordZH'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('last_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('correct', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wrong', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'chinesetool', ['WordSkills'])


    def backwards(self, orm):
        # Removing unique constraint on 'WordTranslation', fields ['word_zh', 'word_pl']
        db.delete_unique(u'chinesetool_wordtranslation', ['word_zh_id', 'word_pl_id'])

        # Removing unique constraint on 'WordZH', fields ['word', 'pinyin']
        db.delete_unique(u'chinesetool_wordzh', ['word', 'pinyin'])

        # Deleting model 'Lesson'
        db.delete_table(u'chinesetool_lesson')

        # Deleting model 'WordPL'
        db.delete_table(u'chinesetool_wordpl')

        # Deleting model 'WordZH'
        db.delete_table(u'chinesetool_wordzh')

        # Deleting model 'WordTranslation'
        db.delete_table(u'chinesetool_wordtranslation')

        # Deleting model 'SentencePL'
        db.delete_table(u'chinesetool_sentencepl')

        # Deleting model 'SentenceZH'
        db.delete_table(u'chinesetool_sentencezh')

        # Deleting model 'SentenceTranslation'
        db.delete_table(u'chinesetool_sentencetranslation')

        # Deleting model 'Abonament'
        db.delete_table(u'chinesetool_abonament')

        # Deleting model 'WordSkills'
        db.delete_table(u'chinesetool_wordskills')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'chinesetool.abonament': {
            'Meta': {'object_name': 'Abonament'},
            'abo_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login_date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'registration_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'chinesetool.lesson': {
            'Meta': {'object_name': 'Lesson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'chinesetool.sentencepl': {
            'Meta': {'object_name': 'SentencePL'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sentence': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'chinesetool.sentencetranslation': {
            'Meta': {'object_name': 'SentenceTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence_pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordPL']"}),
            'sentence_zh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordZH']"})
        },
        u'chinesetool.sentencezh': {
            'Meta': {'object_name': 'SentenceZH'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sentence': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'chinesetool.wordpl': {
            'Meta': {'object_name': 'WordPL'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'chinesetool.wordskills': {
            'Meta': {'object_name': 'WordSkills'},
            'correct': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_time': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'word_zh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordZH']"}),
            'wrong': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'chinesetool.wordtranslation': {
            'Meta': {'unique_together': "(['word_zh', 'word_pl'],)", 'object_name': 'WordTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word_pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordPL']"}),
            'word_zh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordZH']"})
        },
        u'chinesetool.wordzh': {
            'Meta': {'unique_together': "(['word', 'pinyin'],)", 'object_name': 'WordZH'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['chinesetool.Lesson']", 'null': 'True'}),
            'pinyin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'wordpl_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chinesetool.WordPL']", 'through': u"orm['chinesetool.WordTranslation']", 'symmetrical': 'False'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chinesetool']