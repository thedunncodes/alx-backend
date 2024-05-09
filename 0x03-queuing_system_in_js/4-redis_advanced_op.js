import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';


const client = createClient()
    .on('error', err => console.log(
    'Redis client not connected to the server: ERROR_MESSAGE', err
    ))
    .on('connect', () => {
    console.log('Redis client connected to the server');
    });

const hgetall_prom = promisify(client.hgetall).bind(client)
const hashData = (hash, field, value) => {
    client.hset(hash, field, value, redis.print);
};

const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
};

async function main() {
    try {
        for (const [field, value] of Object.entries(hashObj)) {
            hashData('HolbertonSchools', field, value);
        }
        const all_data = await hgetall_prom('HolbertonSchools');
        console.log(all_data)
    } catch (err) {
        console.error(err)
    }
};

main();
