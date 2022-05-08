import settings from "../conf/settings.js"
import RedisManager from "./redis_manager.js";

const Signal = {
    heartbeat: (callback) => {
        let _r = new RedisManager()
        const interval = settings.HEARTBEAT_INTERVAL
        setInterval(async ()=>{
            await _r.client.publish("heartbeat", JSON.stringify({
                "command": "heartbeat",
            }))
            callback()
        }, interval)
    },

    heartbeat_ack: (callback) => {
        let _r = new RedisManager()
        _r = _r.client.duplicate()
        _r.connect()
        _r.subscribe("heartbeat_ack", (msg)=>{
            callback(JSON.parse(msg))
        })
    }
}

export default Signal