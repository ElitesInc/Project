from xml.etree.ElementTree import PI
import space
import pygame
import os 
from space import Monopoly_Space
from space import Monopoly_Property
class Board:
    def __init__(self):
        self.spaces = []
        BOTTOM_Y = 720
        LEFT_X = 90
        TOP_Y = 90
        RIGHT_X = 720


        self.IMAGE = pygame.image.load(os.path.join('Assets', 'monopoly.jpg'))

        GO = Monopoly_Space("GO", RIGHT_X, BOTTOM_Y)
        self.JAIL = Monopoly_Space("Jail", 185, 685)

        #COMMUNITY_CHEST_1 = Monopoly_Community_Chest("Community Chest", 580, BOTTOM_Y)
        #COMMUNITY_CHEST_2 = Monopoly_Community_Chest("Community Chest", LEFT_X, 331)
        #COMMUNITY_CHEST_3 = Monopoly_Community_Chest("Community Chest", 696, 333)
        
        #CHANCE_1 = Monopoly_Chance("Chance", 332, BOTTOM_Y)
        #CHANCE_2 = Monopoly_Chance("Chance", 282, TOP_Y)
        #CHANCE_3 = Monopoly_Chance("Chance", RIGHT_X, 480)

        #LUXURY_TAX = Monopoly_Space("Luxury Tax", 696, 581)
        
        JUST_VISITING = Monopoly_Space("Just Visting", 149, 712)
        INDIA_TOUR = Monopoly_Space("India Tour", LEFT_X, TOP_Y)
        TOURISM_TAX = Monopoly_Space("Tourism Tax", RIGHT_X, TOP_Y)

        
        # ORANGE
        SHANIWAR_WADA = Monopoly_Property("Shaniwar Wada (Orange)", 270, BOTTOM_Y,
        100, 30, 50, (4, 8, 20, 60, 180, 320, 450), space.ORANGE_P, "ORANGE_P")
        RAIGAD_FORT = Monopoly_Property("Raigad Fort (Orange)", LEFT_X,270,
        120, 36, 60, (4, 8, 20, 60, 180, 320, 450), space.ORANGE_P, "ORANGE_P")
        LOTHAL = Monopoly_Property("Lothal(Orange)", 180, BOTTOM_Y,
        70,21,35,(2,4,10,30,90,320,450),space.ORANGE_P,"ORANGE_P")
        KONARK_SUN_TEMPLE = Monopoly_Property("Konark Sun Temple (Orange)", 720, 630,
        90, 27, 45, (2, 4, 10, 30, 90, 320, 450), space.ORANGE_P,"ORANGE_P")

        # LIGHT BLUE
        #ORIENTAL_AVENUE = Monopoly_Property("Oriental Avenue (Light Blue)", 383, BOTTOM_Y,
       # 100, 50, 50, (6, 12, 30, 90, 270, 400, 550), LIGHT_BLUE_P, "LIGHT_BLUE_P")
        #VERMONT_AVENUE = Monopoly_Property("Vermont Avenue (Light Blue)", 285, BOTTOM_Y,
        #100, 50, 50, (6, 12, 30, 90, 270, 400, 550), LIGHT_BLUE_P, "LIGHT_BLUE_P")
        #CONNECTICUT_AVENUE = Monopoly_Property("Connecticut Avenue (Light Blue)", 235, BOTTOM_Y,
        #120, 60, 50, (8, 16, 40, 100, 300, 450, 600), LIGHT_BLUE_P, "LIGHT_BLUE_P")

        # PINK

        CHAR_MINAR = Monopoly_Property("Char Minar (Pink)", 360, BOTTOM_Y,
        80, 24, 40, (10, 20, 50, 150, 450, 625, 750), space.PINK_P, "PINK_P")
        MYSORE_PALACE = Monopoly_Property("Mysore Palace (Pink)", LEFT_X, 630,
        100, 30, 50, (10, 20, 50, 150, 450, 625, 750), space.PINK_P, "PINK_P")
        ELEPHANTA_CAVES = Monopoly_Property("Elephanta Caves (Pink)", 450, TOP_Y,
        70, 21, 35, (12, 24, 60, 180, 500, 700, 900), space.PINK_P, "PINK_P")
        HAWA_MAHAL = Monopoly_Property("Hawa Mahal (Pink)", RIGHT_X, 540,
        90, 27, 45, (12, 24, 60, 180, 500, 700, 900), space.PINK_P, "PINK_P")

        # BROWN

        TAJ_MAHAL = Monopoly_Property("Taj Mahal (Brown)", 180, BOTTOM_Y,
        120, 36, 60, (14, 28, 70, 200, 550, 750, 950), space.BROWN_P, "BROWN_P")
        KANCHIPURAM = Monopoly_Property("Kanchipuram (Brown)", LEFT_X, 450,
        80, 24, 40, (14, 28, 70, 200, 550, 750, 950), space.BROWN_P, "BROWN_P")
        ASHOKA_STUPA = Monopoly_Property("Ashoka Stupa (Brown)", 360, TOP_Y,
        70, 21, 35, (16, 32, 80, 220, 600, 800, 1000), space.BROWN_P, "BROWN_P")
        SAHYADRI_RANGES = Monopoly_Property("Sahyadri Ranges (Brown)", RIGHT_X, 450,
        90, 27, 45, (16, 32, 80, 220, 600, 800, 1000), space.BROWN_P, "BROWN_P")

        # RED

        AGRA_FORT = Monopoly_Property("Agra Fort (Red)", 630, BOTTOM_Y,
        110, 33, 55, (18, 36, 90, 250, 700, 875, 1050), space.RED_P, "RED_P")
        SUNDARBAN = Monopoly_Property("Sundarban (Red)", LEFT_X, 540,
        90, 27, 45, (18, 36, 90, 250, 700, 875, 1050), space.RED_P, "RED_P")
        KAZIRANGA = Monopoly_Property("Kaziranga (Red)", 270, TOP_Y,
        80, 24, 40, (20, 40, 100, 300, 750, 925, 1100), space.RED_P, "RED_P")
        KEDARNATH = Monopoly_Property("Kedarnath (Red)", RIGHT_X,360,
        110,33,55,(20, 40, 100, 300, 750, 925, 1100), space.RED_P, "RED_P")
        # YELLOW

        #ATLANTIC_AVENUE = Monopoly_Property("Atlantic Avenue (Yellow)", 480, TOP_Y,
        #260, 130, 150, (22, 44, 110, 330, 800, 975, 1150), YELLOW_P, "YELLOW_P")
        #VENTNOR_AVENUE = Monopoly_Property("Ventnor Avenue (Yellow)", 530, TOP_Y,
        #260, 130, 150, (22, 44, 110, 330, 800, 975, 1150), YELLOW_P, "YELLOW_P")
        #MARVIN_GARDENS = Monopoly_Property("Marvin Gardens (Yellow)", 630, TOP_Y ,
        #280, 140, 150, (24, 28, 120, 360, 850, 1025, 1200), YELLOW_P, "YELLOW_P")

        # GREEN

        GOLDEN_TEMPLE = Monopoly_Property("Golden Temple (Green)", 450, BOTTOM_Y,
        120, 36, 60, (26, 52, 130, 390, 900, 1100, 1275), space.GREEN_P, "GREEN_P")
        SARNATH = Monopoly_Property("Sarnath (Green)", RIGHT_X, 180,
        70, 21, 35, (26, 52, 130, 390, 900, 1100, 1275), space.GREEN_P, "GREEN_P")
        RUINS_OF_HAMPI = Monopoly_Property("Ruins Of Hampi (Green)", 630, TOP_Y,
        80, 24, 40, (28, 56, 150, 450, 1000, 1200, 1400), space.GREEN_P, "GREEN_P")
        JANTAR_MANTAR = Monopoly_Property("Jantar Mantar (Green)", LEFT_X, 270,
        100, 30, 50, (28, 56, 150, 450, 1000, 1200, 1400), space.GREEN_P, "GREEN_P")

        # BLUE

        CSMT = Monopoly_Property("CSMT (Blue)", 540, BOTTOM_Y,
        110, 33, 55, (50, 100, 200, 600, 1400, 1700, 2000), space.BLUE_P, "BLUE_P")
        DWARKA = Monopoly_Property("Dwarka (Blue)", LEFT_X, 360,
        100, 30, 50, (50, 100, 200, 600, 1400, 1700, 2000), space.BLUE_P, "BLUE_P")
        GOL_GUMBAZ = Monopoly_Property("Gol Gumbaz (Blue)",540, TOP_Y,
        110,33,55,(35, 70, 175, 500, 1100, 1300, 1500), space.BLUE_P, "BLUE_P")
        BASILICA_OF_BOM_JESUS = Monopoly_Property("Basilica Of Bom Jesus (Blue)",RIGHT_X,180,
        120,36,60,(35, 70, 175, 500, 1100, 1300, 1500), space.BLUE_P, "BLUE_P")
        # STATIONS

        #READING_RAILROAD = Monopoly_Railroad("Reading Railroad", 432, BOTTOM_Y, BLACK_P, "BLACK_P")
       #PENNSYLVANIA_RAILROAD = Monopoly_Railroad("Pennsylvania Railroad", LEFT_X, 430, BLACK_P, "BLACK_P")
        #B_O_RAILROAD = Monopoly_Railroad("B & O Railroad", 432, TOP_Y, BLACK_P, "BLACK_P")
        #SHORT_LINE = Monopoly_Railroad("Short Line Railroad", RIGHT_X, 430, BLACK_P, "BLACK_P")

        # UTILITIES

        #ELECTRIC_COMPANY = Monopoly_Utility("Electric Company", LEFT_X, 578, WHITE_P, "WHITE_P")
       # WATER_WORKS = Monopoly_Utility("Water Works", 585, TOP_Y, WHITE_P, "WHITE_P")

        self.places = (GO, AGRA_FORT, CSMT, GOLDEN_TEMPLE, CHAR_MINAR, SHANIWAR_WADA, TAJ_MAHAL, MYSORE_PALACE, SUNDARBAN , KANCHIPURAM, DWARKA ,RAIGAD_FORT, SARNATH,
                 INDIA_TOUR, LOTHAL, KAZIRANGA, ASHOKA_STUPA,ELEPHANTA_CAVES,GOL_GUMBAZ,RUINS_OF_HAMPI,
                 TOURISM_TAX, BASILICA_OF_BOM_JESUS, JANTAR_MANTAR,KEDARNATH, SAHYADRI_RANGES, HAWA_MAHAL, KONARK_SUN_TEMPLE)


