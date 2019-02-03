#! /usr/bin/env python
# -*- coding:utf-8 -*-

import wx
import FramePrincipal
from geolocalisation import *

class EvtFramePrincipal( FramePrincipal.FramePrincipal ):
	def __init__( self, parent ):
		FramePrincipal.FramePrincipal.__init__( self, parent )
		self.localisation = Geolocalisation()
		self.m_textCtrl_adresse.SetValue("103 Rue de Prague, 59800 Lille")
		self.m_textCtrl_origine.SetValue("103 Rue de Prague, 59800 Lille")
		self.m_textCtrl_destination.SetValue("23 Rue de la Performance, 59666 Villeneuve d'Ascq")


	def Rechercher( self, event ):
		self.m_listBox_localisation.Clear()
		#self.m_button_rechercher.Disable()

		adresse = self.m_textCtrl_adresse.GetValue()
		param = self.localisation.geolocalisationAdresse(adresse)

		self.m_listBox_localisation.Append("Ville :       "+param[0])
		self.m_listBox_localisation.Append("Rue :         "+param[1])

		Num_rue = str(param[2])
		self.m_listBox_localisation.Append("Num de rue :  "+Num_rue)
		self.m_listBox_localisation.Append("Code Postal : "+param[3])
		self.m_listBox_localisation.Append("Pays :        "+param[4])
		self.m_listBox_localisation.Append("Région :      "+param[6])
		self.m_listBox_localisation.Append("Département : "+param[8])

		lat = str(param[9])
		lng = str(param[10])

		self.m_listBox_localisation.Append("Latitude :     "+lat)
		self.m_listBox_localisation.Append("Longitude :    "+lng)

		self.m_button_rechercher.Enable()

	pass

	def Estimation( self, event ):

		self.m_listBox2.Clear()
		self.m_listBox4.Clear()
		self.m_listBox3.Clear()

		origine = self.m_textCtrl_origine.GetValue()
		destination = self.m_textCtrl_destination.GetValue()

		ModeVoiture = self.localisation.GetModeVoiture(origine,destination)
		ModeVelo = self.localisation.GetModeVelo(origine,destination)
		ModeMarcheAPied = self.localisation.GetModeMarcheAPied(origine,destination)

		distanceKmVoiture = str(ModeVoiture[0])
		distanceMVoiture = str(ModeVoiture[1])
		DureeEnVoiture = str(ModeVoiture[2])

		self.m_listBox2.Append("Distance en Km :  "+distanceKmVoiture)
		self.m_listBox2.Append("Distance en m :   "+distanceMVoiture)
		self.m_listBox2.Append("Durée du trajet : "+DureeEnVoiture)

		distanceKmVelo = str(ModeVelo[0])
		distanceMVelo = str(ModeVelo[1])
		DureeVelo  = str(ModeVelo[2])


		self.m_listBox4.Append("Distance en Km :  "+distanceKmVelo)
		self.m_listBox4.Append("Distance en m :   "+distanceMVelo)
		self.m_listBox4.Append("Durée du trajet : "+DureeVelo)

		distanceKmAPied = str(ModeMarcheAPied[0])
		distanceMAPied = str(ModeMarcheAPied[1])
		DureeAPied = str(ModeMarcheAPied[2])


		self.m_listBox3.Append("Distance en Km :  "+distanceKmAPied)
		self.m_listBox3.Append("Distance en m :   "+distanceMAPied)
		self.m_listBox3.Append("Durée du trajet : "+DureeAPied)
	pass
