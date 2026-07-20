"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.request = exports.setupAki = void 0;
const axios_1 = __importDefault(require("axios"));
const Config_1 = require("../constants/Config");
const cheerio_1 = require("cheerio");
const headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
};
const axiosConfig = {
    validateStatus: () => true
};
const setupAki = async (region, childMode, config) => {
    try {
        const [lang, theme] = region.split("_");
        const baseUrl = `https://${lang}.akinator.com`;
        const sid = Config_1.themes[theme] ?? 1;
        const { data } = await axios_1.default.post(`${baseUrl}/game`, new URLSearchParams(Object.entries({
            cm: childMode === true,
            sid
        })), { headers: { ...headers, ...config.headers }, ...config });
        const $ = (0, cheerio_1.load)(data);
        const session = $("#askSoundlike > #session").attr("value");
        const signature = $("#askSoundlike > #signature").attr("value");
        const question = $("#question-label").text();
        return { session, signature, question, baseUrl, sid };
    }
    catch (e) {
        console.log(e);
    }
};
exports.setupAki = setupAki;
const request = async (url, body, config) => axios_1.default.post(url, body, {
    headers: { ...headers, ...config.headers },
    ...axiosConfig
});
exports.request = request;
