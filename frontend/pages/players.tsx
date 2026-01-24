import { useEffect, useState } from "react";
import PlayerTimeseriesChart from "../components/PlayerTimeseriesChart";
import Layout from "../components/Layout";

export default function PlayerPage() {
  const [chartData, setChartData] = useState<any[]>([]);

  useEffect(() => {
    async function loadTimeseries() {
      const res = await fetch(
        "http://127.0.0.1:8001/players/1628983/timeseries"
      );
      const apiData = await res.json();

      const transformed = apiData.dates.map((date: string, i: number) => ({
        date,
        fantasy_points: apiData.fantasy_points[i],
        rolling_FPoint_Last5: apiData.rolling_FPoint_Last5[i],
        rolling_FPoint_Last10: apiData.rolling_FPoint_Last10[i],
      }));

      setChartData(transformed);
    }

    loadTimeseries();
  }, []);

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-6">
        Player Performance
      </h1>

      <PlayerTimeseriesChart data={chartData} />
    </Layout>
  );
}
