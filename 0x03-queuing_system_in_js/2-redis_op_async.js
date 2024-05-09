import { createClient } from 'redis';
import redis from 'redis'
import { promisify } from 'util'


const client = createClient()
.on('error', err => console.log(
  'Redis client not connected to the server: ERROR_MESSAGE', err
))
.on('connect', () => {
  console.log('Redis client connected to the server');
});

const get_prom = promisify(client.get).bind(client)

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await get_prom(schoolName) 
    console.log(reply);
  } catch (err) {
    console.error('Key Not present: ', err);
  };
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
