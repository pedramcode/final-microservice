import RedisManager from "./core/redis_manager.js"
import Signal from "./core/signal.js"
import mongoose from "mongoose"
import settings from "./conf/settings.js"
import Service from "./models/service.js"
import express from "express"
import cors from "cors"

mongoose.connect(settings.DATABASE,
    {},
    ()=>{
        console.log("Database is connected")
    }
)

const app = express()
app.use(cors)

Signal.heartbeat(async ()=>{
    let dt = new Date();
    let dt2 = new Date();
    dt.setSeconds(dt.getSeconds() - (settings.HEARTBEAT_INTERVAL/1000))
    dt2.setSeconds(dt2.getSeconds() - (settings.HEARTBEAT_INTERVAL/1000) * 20)
    await Service.updateMany({last_ack: {$lte: dt}}, {$set: {up: false}}).exec()
    await Service.deleteMany({last_ack: {$lte: dt2}}).exec()
})

Signal.heartbeat_ack(async (data)=>{
    let service = await Service.findOne({name: data.name})
    if(!service){
        service = await Service.create({
            service: data.service,
            name: data.name,
            host: data.host,
            port: data.port,
            last_ack: Date.now(),
            up: true,
        })
    }
    service.last_ack = Date.now()
    service.up = true
    await service.save()
})

