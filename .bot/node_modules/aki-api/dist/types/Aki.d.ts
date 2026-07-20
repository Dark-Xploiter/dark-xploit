import { AxiosRequestConfig } from "axios";
import { region } from "../constants/Config";
export interface AkinatorConstructor {
    region?: region;
    childMode?: boolean;
    config?: AxiosRequestConfig;
}
export interface ResponseSetupAki {
    session: string;
    signature: string;
    question: string;
    baseUrl: string;
    sid: number;
}
export declare enum AkinatorAnswer {
    "Yes" = 0,
    "No" = 1,
    "Don't know" = 2,
    "Probably" = 3,
    "Probably not" = 4
}
export interface AkinatorAPIAnswerResponse {
    status: number;
    data: {
        completion: "OK" | "KO" | "SOUNDLIKE";
        akitude: string;
        step: string;
        progression: string;
        question_id: string;
        question: string;
        id_proposition: string;
        id_base_proposition: string;
        valide_contrainte: string;
        name_proposition: string;
        description_proposition: string;
        flag_photo: string;
        photo: string;
        pseudo: string;
        nb_elements: number;
    };
}
export interface AkinatorAPICancelAnswerResponse {
    status: number;
    data: {
        akitude: string;
        step: string;
        progression: string;
        question_id: string;
        question: string;
    };
}
