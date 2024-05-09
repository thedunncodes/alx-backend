import { createClient } from 'redis';

const client = createClient()
    .on('error', err => console.log(
    'Redis client not connected to the server: ERROR_MESSAGE', err
    ))
    .on('connect', () => {
    console.log('Redis client connected to the server');
    });

const subscribe = (channel) => {
    client.subscribe(channel)
}

subscribe('holberton school channel')
client.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit()
    }
    console.log(`${message}`);
});
