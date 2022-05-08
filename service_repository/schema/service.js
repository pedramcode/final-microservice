import mongoose from "mongoose";

const ServiceSchema = mongoose.Schema({
    service: {type: String, required:true},
    name: {type: String, required:true},
    last_ack: {type: Date, required:true},
    host: {type: String, required:true},
    port: {type: Number, required:true},
    up: {type: Boolean, default: true},
    protocol: {type: String, default: "gRPC"}
})

export default ServiceSchema