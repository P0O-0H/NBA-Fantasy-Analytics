import type { NextApiRequest, NextApiResponse } from "next";

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({
    players: [
      {
        name: "Immanuel Quickley",
        team: "TOR",
        score: 18.4,
        reason: "Massive usage spike with injuries."
      },
      {
        name: "Dereck Lively",
        team: "DAL",
        score: 16.2,
        reason: "More minutes with Kyrie out."
      }
    ]
  });
}
