# -*- coding: utf-8 -*-

# Copyright (C) 2015 ZetaOps Inc.

__author__ = 'Ozgur Firat Cinar'

from zato.server.service import Service
from zato.common import DATA_FORMAT
import os
from time import sleep
import urllib2
import socket
from json import loads, dumps

os.environ["PYOKO_SETTINGS"] = 'ulakbus.settings'
from ulakbus.models.hitap import HizmetKayitlari

H_USER = os.environ["HITAP_USER"]
H_PASS = os.environ["HITAP_PASS"]


class HizmetCetveliUpdate(Service):
    """
    HITAP HizmetCetveliUpdate Zato Servisi
    """

    def handle(self):
        # Save a dictionary into a pickle file.
        import pickle

        self.logger.info("zato service started to work.")

        tckn = self.request.payload['tckn']
        update_credentials = self.request.payload['update_credentials']

        # self.logger.info("Payload tckn: %s" % tckn)
        # self.logger.info("Update credentials: %s" % update_credentials)

        dict_to_save = update_credentials

        pickle.dump(dict_to_save, open("hitap_update_backup.p", "wb"))

        rescued_dict = pickle.load(open("hitap_update_backup.p", "rb"))

        self.logger.info("RESCUED DATA: %s" % rescued_dict)

        conn = self.outgoing.soap['HITAP'].conn

        # service_record = HizmetKayitlari.objects.filter(kayit_no=KAYIT_NO).get()

        '''
        Tckn = TCKN,
        kayitNo = KAYIT_NO,
        baslamaTarihi = BASLAMA_TARIHI,
        bitisTarihi = BITIS_TARIHI,
        gorev = GOREV,
        unvanKod = UNVAN_KOD,
        yevmiye = YEVMIYE,
        ucret = UCRET,
        hizmetSinifi = HIZMET_SINIFI,
        kadroDerece = KADRO_DERECE,
        odemeDerece = ODEME_DERECE,
        odemeKademe = ODEME_KADEME,
        odemeEkgosterge = ODEME_EK_GOSTERGE,
        kazanilmisHakAyligiDerece = KAZANILMIS_HAK_AYLIGI_DERECE,
        kazanilmisHakAyligiKademe = KAZANILMIS_HAK_AYLIGI_KADEME,
        kazanilmisHakAyligiEkgosterge = KAZANILMIS_HAK_AYLIGI_EK_GOSTERGE,
        hizmetSinifi = HIZMET_SINIFI,
        emekliDerece = EMEKLI_DERECE,
        emekliKademe = EMEKLI_KADEME,
        emekliEkgosterge = EMEKLI_EK_GOSTERGE,
        sebepKod = SEBEP_KOD,
        kurumOnayTarihi = KURUM_ONAY_TARIHI,
        kullaniciAd = KULLANICI_AD,
        sifre = SIFRE


        TCKN
        KAYIT_NO
        BASLAMA_TARIHI
        BITIS_TARIHI
        GOREV
        UNVAN_KOD
        YEVMIYE
        UCRET
        HIZMET_SINIFI
        KADRO_DERECE
        ODEME_DERECE
        ODEME_KADEME
        ODEME_EK_GOSTERGE
        KAZANILMIS_HAK_AYLIGI_DERECE
        KAZANILMIS_HAK_AYLIGI_KADEME
        KAZANILMIS_HAK_AYLIGI_EK_GOSTERGE
        HIZMET_SINIFI
        EMEKLI_DERECE
        EMEKLI_KADEME
        EMEKLI_EK_GOSTERGE
        SEBEP_KOD
        KURUM_ONAY_TARIHI
        KULLANICI_AD
        SIFRE
        '''

        with conn.client() as client:
            service_bean = client.service.HizmetCetvelUpdate(Tckn=TCKN,
                                                             kayitNo=KAYIT_NO,
                                                             baslamaTarihi=BASLAMA_TARIHI,
                                                             bitisTarihi=BITIS_TARIHI,
                                                             gorev=GOREV,
                                                             unvanKod=UNVAN_KOD,
                                                             yevmiye=YEVMIYE,
                                                             ucret=UCRET,
                                                             hizmetSinifi=HIZMET_SINIFI,
                                                             kadroDerece=KADRO_DERECE,
                                                             odemeDerece=ODEME_DERECE,
                                                             odemeKademe=ODEME_KADEME,
                                                             odemeEkgosterge=ODEME_EK_GOSTERGE,
                                                             kazanilmisHakAyligiDerece=KAZANILMIS_HAK_AYLIGI_DERECE,
                                                             kazanilmisHakAyligiKademe=KAZANILMIS_HAK_AYLIGI_KADEME,
                                                             kazanilmisHakAyligiEkgosterge=KAZANILMIS_HAK_AYLIGI_EK_GOSTERGE,
                                                             hizmetSinifi=HIZMET_SINIFI,
                                                             emekliDerece=EMEKLI_DERECE,
                                                             emekliKademe=EMEKLI_KADEME,
                                                             emekliEkgosterge=EMEKLI_EK_GOSTERGE,
                                                             sebepKod=SEBEP_KOD,
                                                             kurumOnayTarihi=KURUM_ONAY_TARIHI,
                                                             kullaniciAd=KULLANICI_AD,
                                                             sifre=SIFRE).HizmetCetveliServisBean

        self.logger.info("HizmetCetveliGetir started to work.")

        '''
        for k, v in hitap_dict.items():
            if k not in local_records:
                print "Bu kayit localde yok! => " + str(k)

        for k, v in local_records.items():
            if k not in hitap_dict:
                print "Bu kayit hitapta yok! => " + str(k)
        '''

        self.logger.info("zato service finished.")
