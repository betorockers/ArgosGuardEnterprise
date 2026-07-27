import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '5s', target: 20 },
    { duration: '10s', target: 20 },
    { duration: '5s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  const BASE_URL = 'http://127.0.0.1:8000';

  const res = http.get(`${BASE_URL}/security/login/`);
  check(res, {
    'status is 200 or 302': (r) => r.status === 200 || r.status === 302,
  });

  sleep(1);
}
