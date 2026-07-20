import { AxiosRequestConfig } from "axios";
import { region } from "../constants/Config";
import { ResponseSetupAki } from "../types/Aki";
export declare const setupAki: (region: region, childMode: boolean, config: AxiosRequestConfig) => Promise<ResponseSetupAki>;
export declare const request: <data>(url: string, body: any, config: AxiosRequestConfig) => Promise<data>;
