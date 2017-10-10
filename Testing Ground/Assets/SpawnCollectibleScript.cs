using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnCollectibleScript : MonoBehaviour {

	//create an array of spawn points, assigned in inspector
	public Transform[] SpawnPointArray;
	//wait time before coin is spawned
	public float spawnTime = 1.5f;

	public GameObject Coin;

	void Start()
	{
		Invoke ("SpawnCoin", spawnTime);
	}
	
	void Update () {
		
	}

	void SpawnCoin() {
		int spawnIndex = Random.Range(0,SpawnPointArray.Length);
		Instantiate (Coin,SpawnPointArray[spawnIndex].position,SpawnPointArray[spawnIndex].rotation);
	}
}
