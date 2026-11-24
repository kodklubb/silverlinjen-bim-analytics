const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export class ApiError extends Error {
  constructor(
    message: string,
    public readonly status: number
  ) {
    super(message);
    this.name = "ApiError";
  }
}

export async function apiGet(
  endpoint: string,
  signal?: AbortSignal
): Promise<unknown> {
  if (!API_BASE_URL) {
    throw new Error(
      "NEXT_PUBLIC_API_URL is not configured."
    );
  }

  const baseUrl = API_BASE_URL.replace(/\/+$/, "");
  const path = endpoint.replace(/^\/+/, "");

  const response = await fetch(`${baseUrl}/${path}`, {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
    cache: "no-store",
    signal,
  });

  if (!response.ok) {
    throw new ApiError(
      `API request failed: ${response.statusText}`,
      response.status
    );
  }

  const data: unknown = await response.json();

  return data;
}