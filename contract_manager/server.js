import express from "express"
import settings from "./conf/settings.js"
import fs from "fs"
import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express()

app.get("/contract/:contract", (req, res)=>{
    const repo_data = JSON.parse(fs.readFileSync(path.join(__dirname, "repository.json"), 'utf-8'))
    if(!req.params.contract || !repo_data[req.params.contract]){
        res.setHeader("content-type", "application/json")
        res.status(404)
        return res.send(JSON.stringify({
            "error": "Contract not found"
        }))
    }
    try {
        const contract_data = fs.readFileSync(path.join(__dirname, repo_data[req.params.contract]), 'utf-8')
        res.setHeader("content-type", "text/plain")
        res.status(200)
        res.send(contract_data)
    }catch (ex){
        res.setHeader("content-type", "application/json")
        res.status(404)
        return res.send(JSON.stringify({
            "error": "Contract not found"
        }))
    }

})

app.listen(settings.REST_PORT, settings.REST_HOST)