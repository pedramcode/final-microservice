import {createClient} from "redis";
import settings from "../conf/settings.js";


export default class RedisManager{
    constructor() {
        this.client = createClient({
            socket: {
                host: settings.REDIS_HOST,
                port: settings.REDIS_PORT,
            },
            database: 0,
        })
        this.client.connect().then(()=>{
        }).catch(()=>{
            console.error("Something is wrong with redis connection")
        })
    }
}
