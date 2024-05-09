import { createClient } from 'redis';
import redis from 'redis'

const client = createClient()
  .on('error', err => console.log(
    'Redis client not connected to the server: ERROR_MESSAGE', err
))
  .on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        if (err) console.error("ERROR: ", err)
            
        console.log(reply)
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
