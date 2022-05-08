import mongoose from "mongoose"
import ServiceSchema from "../schema/service.js"


const Service = mongoose.model('Service', ServiceSchema)

export default Service