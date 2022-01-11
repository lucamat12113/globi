/**
 * @file louscoot.h
 * @author Luca Matagne
 * @brief ADT to manage a fleet of scooter
 * @version 0.1
 * @date 2021-11-23
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#ifndef __LOUSCOOT_T__
#define __LOUSCOOT_T__



 /*louer
 rendre
 etat scooter
 etat parc (+ moyenne km et nbr de scoot au depot)
*/

/**
 * @struct scooter 
 * @brief data structur which represant a scooter.
 * ( a model, an identification number, km and home or traveling)
 * 
 */

typedef struct Scooter_t Scooter;

/**
 * @fn Scooter *create(char modele, int id_nb, float km);
 * @brief creates an instance of a scooter 
 * 
 * @param model, the model of the scooter (!=NULL)
 * @param id_nbr, identification number of the scooter (!=NULL)
 * @param km, dista,ce traveled by the scooter (>=0)
 * 
 * @return a scooter that is able to be located (NULL othherwise)
 */
Scooter *create(char *model, int id_nbr, float km);

/**
 * @fn int get_position(int id_nbr);
 * @brief tell if the scooter is traveeling or not.
 * 
 * @param id_nbr, identification number of the scooter that we want to know the position
 * 
 * @return 1 or 2, 1 if the scooter is available. 2 if the scooter is in renting
 */
int get_position(int id_nbr);

/**
 * @fn 
 * @brief 
 * 
 * 
 */




#endif