using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SpawnCollectibleScript : MonoBehaviour {

	private UnityEngine.AI.NavMeshAgent agent;
	//create an array of spawn points, assigned in inspector
	public Transform[] SpawnPointArray;
	//create an array of exit points
	public Transform[] exitPointArray;
	//create an array to hold the cop objects
	public GameObject[] cops;
	//wait time before coin is spawned
	public float spawnTime = 1.5f;
	private int spawnIndex;

	public GameObject Coin;

	void Start()
	{
		agent = GetComponent<UnityEngine.AI.NavMeshAgent>();
		agent.autoBraking = false;
		Invoke ("SpawnCoin", spawnTime);
	}
	
	void Update ()
	{
		
	}

	void SpawnCoin()
	{
	    spawnIndex = Random.Range (0, SpawnPointArray.Length);
		Instantiate (Coin,SpawnPointArray[spawnIndex].position,SpawnPointArray[spawnIndex].rotation);
		collectCoin();
	}

	void collectCoin()
	{
		// Set the agent to go to the spawned coin's position.
		agent.destination = SpawnPointArray[spawnIndex].position;

	}

	void Escape()
	{
		if (SpawnPointArray [spawnIndex].CompareTag ("A")) {
			agent.destination = exitPointArray [0].transform.position;
		}
		if (SpawnPointArray [spawnIndex].CompareTag ("B")) {
			agent.destination = exitPointArray [1].transform.position;
		}
		if (SpawnPointArray [spawnIndex].CompareTag ("C")) {
			agent.destination = exitPointArray [2].transform.position;
		}
		if (SpawnPointArray [spawnIndex].CompareTag ("D")) {
			agent.destination = exitPointArray [3].transform.position;
		}
		if (SpawnPointArray [spawnIndex].CompareTag ("E")) {
			agent.destination = exitPointArray [4].transform.position;
		}
	}

	void Chase()
	{
		for (int i; i < cops.Length; i++)
		{
			
		}
	}

	void OnTriggerEnter (Collider other)
	{
		if (other.gameObject.CompareTag("Coin"))
		{
			Destroy(other.gameObject);		
			Escape();
			Chase();
		}
	}

	void OnCollisionEnter (Collision other)
	{
		if (other.gameObject.CompareTag ("Cop"))
		{
			Destroy (this.gameObject);	
		}

	}
}
