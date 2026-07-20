"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Akinator = void 0;
const Config_1 = require("./constants/Config");
const Request_1 = require("./functions/Request");
class Akinator {
    constructor({ region = "en", childMode, config }) {
        this.config = {};
        if (!Config_1.regions.includes(region))
            throw new Error("Please insert a correct region!");
        this.step = 0;
        this.region = region;
        this.childMode = childMode;
        this.progress = 0.0;
        if (config)
            this.config = config;
    }
    async start() {
        const { session, signature, question, baseUrl, sid } = await (0, Request_1.setupAki)(this.region, this.childMode, this.config);
        if (!session || !signature || !question)
            throw new Error("Failed to get session and signature");
        this.session = session;
        this.signature = signature;
        this.baseUrl = baseUrl;
        this.sid = sid;
        this.question = question;
    }
    async answer(answ) {
        const data = {
            step: this.step,
            progression: this.progress,
            sid: this.sid,
            cm: this.childMode === true,
            answer: answ,
            step_last_proposition: this.step_last ?? "",
            session: this.session,
            signature: this.signature
        };
        const { status, data: result } = await (0, Request_1.request)(this.baseUrl + "/answer", data, this.config);
        if (status != 200 || result.completion !== "OK")
            throw new Error("Failed making request, status : " + status);
        if (result.id_proposition) {
            this.sugestion_name = result.name_proposition;
            this.sugestion_desc = result.description_proposition;
            this.sugestion_photo = result.photo;
            this.isWin = true;
        }
        else {
            this.step = parseInt(result.step);
            this.progress = parseFloat(result.progression);
            this.question = result.question;
        }
    }
    async cancelAnswer() {
        const data = {
            step: this.step,
            progression: this.progress,
            sid: this.sid,
            cm: this.childMode === true,
            session: this.session,
            signature: this.signature
        };
        const { status, data: result } = await (0, Request_1.request)(this.baseUrl + "/cancel_answer", data, this.config);
        if (status != 200)
            throw new Error("Failed making request, status : " + status);
        this.step = parseInt(result.step);
        this.progress = parseFloat(result.progression);
        this.question = result.question;
    }
}
exports.Akinator = Akinator;
